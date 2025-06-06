#imports
from blueprints.blueprint_template import *

#makes blueprint object
auth = setup("auth")

#user area
@auth.route('/user')
@login_required
def user_area():
    return render_template("user_area.html")

#sign users out
@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("non_auth.index"))

#various admin things
@auth.route('/admin')
@login_required
def admin():
    if not current_user.username == "sam":
        return redirect(url_for("auth.user_area"))

    to_enable = User.query.filter_by(
        account_enabled=False
        ).all()
    return render_template("admin.html", to_enable=to_enable)