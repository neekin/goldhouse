from application import createApp, db
from flask_migrate import Migrate
from models import Member,OauthMemberBind

app = createApp()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.logger.info('一切正常,可以飙车')
    app.run()
