# PlanetScale
# name: test
# host: aws.connect.psdb.cloud
# username: pib8yr4mgeklm4f5eosa
# password: pscale_pw_wJ29lH3O8SfQdUZIz5dMuYvYxR8vl8vgZRYk34VbTui

import sqlalchemy
from sqlalchemy import create_engine, text

connection_string = "mysql+pymysql://pib8yr4mgeklm4f5eosa:pscale_pw_wJ29lH3O8SfQdUZIz5dMuYvYxR8vl8vgZRYk34VbTui@aws.connect.psdb.cloud/test"
#secure connection (ssl) is required
ssl = {
    "ca": "/etc/ssl/cert.pem"
    }

engine = create_engine(connection_string, 
                       connect_args={
                            "ssl" : {
                                "ssl_ca": "/etc/ssl/cert.pem"
                            }
                        })

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())