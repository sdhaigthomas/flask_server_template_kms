#imports
from blueprints.blueprint_template import *
from utils.signup_val import signup_val
from utils.password_val import password_val

#makes blueprint object
non_auth = setup("non_auth")

#home page
@non_auth.route('/')
def index():
    return render_template("index.html")

#signin page
@non_auth.route('/signin', methods=["POST","GET"])
def signin():
    #shorten long function
    get = request.form.get

    #assign key varibles
    username = get("username")
    password = get("password")

    #has anything been sent back?
    if username or password:
        #check if all has been submitted, and prompt if not
        if not username: flash("Enter a username as well as a password")
        elif not username: flash("Enter a password as well as a username")
        else:
            #all has been submitted
            user = User.query.filter_by(
                username=username
                ).first()
            #Is the user registred, and does password match
            if user and check(
                original_string=password, 
                candidate_hash=user.password
                ):
                #login user and send them to the user area
                login_user(user, remember=True)
                return redirect(url_for("auth.user_area"))

            #tell user that their details are wrong!
            else: flash("Username and/or password is incorrect")
    return render_template("signin.html")

#signup page
@non_auth.route('/signup', methods=["POST","GET"])
def signup():
    if request.form.get("username"):
        #shorten
        get = request.form.get

        #send form to validator
        form_OK = signup_val(get=get, User=User, password_val=password_val, username_val=username_val)

        #flash any issues found by the func
        if form_OK[0] == False:
            #send the user what the issue is
            flash(form_OK[1])

        else:
            #all OK, add data to db
            db.session.add(
                User(username=get("username"),password=make_hash(get("password")))
            )
            db.session.commit()
            return redirect(url_for("non_auth.signin"))# add a redirect to user area.

    return render_template("signup.html")



