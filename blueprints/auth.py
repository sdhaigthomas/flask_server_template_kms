#imports
from blueprints.blueprint_template import *

#makes blueprint object
auth = setup("auth")

#user area
@auth.route('/user')
@login_required
def user_area():
    return render_template("user_area.html")

#user area
@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("non_auth.index"))