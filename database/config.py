from configparser import ConfigParser


def db_config(filename="db.ini", section="postgresql"):
    """
    Parse the PostgreSQL config file to connect to database.
    """

    # create a parser
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            f"The file {filename} does not contain any section of name: {section}!"
        )

    return db
