from pydantic import BaseModel , Field 
import sqlite3 as sql
from mcp.server.fastmcp import FastMCP
import re 

# lets create the MCP Server 

server = FastMCP('Secure-SQL-Agent')

DB_PATH = r"YOUR DATABASE PATH is here"

class QueryInput(BaseModel):
    sql_query : str = Field(description='Tell me the SQL Query you want to run in the database')

# Setting up the Security Guard rail 

def is_query_safe(query:str)-> bool :
    query_lower = query.lower()
    forbidden_keywords = ["drop", "delete", "update", "insert", "alter", "truncate", "create"]
    for word in forbidden_keywords :
        if re.search(r'\b'+re.escape(word)+r'\b', query_lower):
            return False 
    return True 

@server.tool(title="Get the database schema")
def get_db_schema () -> str:
    """ It generally provides the schema of the tables and all the associated columns in the table 
    Make sure to run the above schema before running a query , to get the details of it 
    """
    database = sql.connect(DB_PATH)
    cursor = database.cursor()

    try:
        cursor.execute("SELECT sql FROM sqlite_master WHERE type ='table'; ") 
        schemas = cursor.fetchall()
        schema_text=""
        for schema in schemas:
            if schema[0]:
                schema_text += f"{schema[0]}\n\n"
        return schema_text
    except Exception as e :
        return f"Unable to load the Schema and we are facing error loading the schema, Error: {str(e)}"
    finally:
        database.close()
@server.tool(title='Running the Sql Query')
def run_sql_query(input_data:QueryInput) ->  str:
    """ Run your Sql Queries and see the output in the Users database """
    query = input_data.sql_query
    if not is_query_safe(query=query):
        return "SECURITY VIOLATION !!! , We cannot proceed with the query as it is unsafe for the database"
    database = sql.connect(DB_PATH)
    cursor = database.cursor()
    try :
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [description[0]for description in cursor.description]
        result = f"Query Results , we have for {query} is "
        result += " | ".join(columns) + "\n" + "-" * 40 + "\n"
        
        for row in rows:
            result += " | ".join(str(item) for item in row) + "\n"
            
        return result if rows else "Query executed successfully, but returned 0 rows."
    except Exception as e :
        return f"SQL Error as : {str(e)}"
    finally:
        database.close()
if __name__ == "__main__":
    server.run()


