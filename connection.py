import sqlalchemy
from sqlalchemy import create_engine, text


class Connection:
    def __init__(self):
        self.engine = create_engine('mysql://root:ChristianSchindl1@softwareishell.com/catinder?charset=utf8mb4')
        self.connection = self.engine.connect()

    def pull_cat_image(self):
        result = self.connection.execute(text("SELECT Image FROM Cats "
                                              "ORDER BY RAND() "
                                              "LIMIT 1"))
        result = str(result.fetchone())
        result = result.split("'")
        result = result[1]
        return result


conn = Connection()