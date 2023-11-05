import requests

informatics_user = "cmsUser"
informatics_password = "1m49zD*YNlNsaDa5"
informatics_host = "http://localhost:8080"


def register_task(appid, cms_id, logger):
    params = {
        "cmsID": cms_id,
        "appID": appid
    }
    session = _get_session()
    try:
        session.post(f"{informatics_host}/cms-api/register-task", json=params)
    except:
        return

def register_submission(cms_id, appid):
    params = {
        "cmsID": cms_id,
        "appID": appid
    }
    session = _get_session()
    try:
        session.post(f"{informatics_host}/cms-api/register-submission", json=params)
    except:
        return

def send_submission_compilation_result(cms_id, compilation_result, compilation_message):
    params = {
        "cmsID": cms_id,
        "result": compilation_result,
        "message": compilation_message
    }
    session = _get_session()
    try:
        session.post(f"{informatics_host}/cms-api/submission-compilation-result", json=params)
    except:
        return

def send_submission_result(cms_id, score, submission_message):
    params = {
        "cmsID": cms_id,
        "score": score,
        "submissionResult": submission_message
    }
    session = _get_session()
    try:
        session.post(f"{informatics_host}/cms-api/submission-result", json=params)
    except:
        return

def update_submission_test(submission_id, test_number):
    params = {
        "cmsID": submission_id,
        "testNumber": test_number
    }
    session = _get_session()
    try:
        session.post(f"{informatics_host}/cms-api/update-submission-test", json=params)
    except:
        return

def _get_session():
    session = requests.Session()
    session.auth = (informatics_user, informatics_password)
    return session
