import app
import waitress 



waitress.serve(app.create_app())
