from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://@aws.connect.psdb.cloud/website_data?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args={
        "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


with engine.connect() as conn:
    result = conn.execute(text("select * from skills"))
    print(result.all())
