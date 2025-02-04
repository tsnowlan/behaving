import os
from behaving import environment as benv


def before_all(context):
    import behaving

    context.remote_webdriver_url = "http://selenium-hub:4444"
    context.default_browser = "firefox"
    context.accept_ssl_certs = True

    context.attachment_dir = os.path.join(
        os.path.dirname(behaving.__file__), "../../tests/data"
    )
    context.sms_path = os.path.join(
        os.path.dirname(behaving.__file__), "../../var/sms/"
    )
    context.mail_path = os.path.join(
        os.path.dirname(behaving.__file__), "../../var/mail/"
    )
    context.gcm_path = os.path.join(
        os.path.dirname(behaving.__file__), "../../var/gcm/"
    )
    context.screenshots_dir = os.path.join(
        os.path.dirname(behaving.__file__), "../../var/screenshots/"
    )
    benv.before_all(context)


def after_all(context):
    benv.after_all(context)


def before_feature(context, feature):
    benv.before_feature(context, feature)


def after_feature(context, feature):
    benv.after_feature(context, feature)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    benv.after_scenario(context, scenario)
