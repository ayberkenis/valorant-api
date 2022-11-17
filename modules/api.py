from flask import Blueprint, request, jsonify, url_for, current_app, send_from_directory
import time
import valorant
from valorant import ValorantAPI

bp = Blueprint('api', __name__, url_prefix='/valorant-api')


@bp.route('/rank/<username>/<tag>', methods=['GET'])
@bp.route('/rank/<username>/<tag>/<region>', methods=['GET'])
def get_user_mmr(username, tag):
    try:
        if request.args.get('language'):
            language = request.args.get('language')
        else:
            language = 'tr-TR'
        val = valorant.ValorantAPI(username, tag, language=language)
        data = val.get_mmr_info()
        return data
    except Exception as e:
        if isinstance(e, AttributeError):
            return "API'de anlık bir hata oluştu, lütfen birkaç dakika sonra tekrar deneyin."
        else:
            return "API'de oluşan problem nedeniyle veri çekilemedi, lütfen daha sonra tekrar deneyin."


@bp.route('/match/<username>/<tag>', methods=['GET'])
@bp.route('/match/<username>/<tag>/<region>', methods=['GET'])
def get_user_match(username, tag, region="eu"):
    try:
        start = time.time()
        if request.args.get('language'):
            language = request.args.get('language')
        else:
            language = 'tr-TR'
        val = valorant.ValorantAPI(username, tag, language=language)
        data = val.get_last_match()
        print(f"Time: {time.time() - start}")
        return data
    except Exception as e:
        if isinstance(e, AttributeError):
            return "API'de anlık bir hata oluştu, lütfen birkaç dakika sonra tekrar deneyin."
        else:
            return "API'de oluşan problem nedeniyle veri çekilemedi, lütfen daha sonra tekrar deneyin."


@bp.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'ok', 'message': 'Welcome to Valorant InGame API! For more information, visit https://docs.ayberkenis.com.tr/apis/valorant'}), 200