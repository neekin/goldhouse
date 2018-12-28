from . import api_index
from flask import request, jsonify, json
from flask import current_app
import requests
from models.OauthMemberBind import OauthMemberBind
from models.Member import Member


@api_index.route('/member/login', methods=["GET", "POST"])
def login():
    req = request.values
    result = {'code': 200, 'msg': '授权成功', 'data': req}
    # current_app.logger.info(req)
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        result['code'] = -1
        result['msg'] = '需要code'
        return jsonify(result)
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code' \
        .format(current_app.config['MINA_APP']['appid'], current_app.config['MINA_APP']['appSecret'], code)

    r = requests.get(url)
    rjson = json.loads(r.text)
    openid = rjson['openid']
    bind_info = OauthMemberBind.query.filter_by(openid=openid).first()
    if not bind_info:
        model_member = Member()
        model_member.nickName = req['nickName']
        model_member.gender = req['gender']
        model_member.province = req['province']
        model_member.city = req['city']
        model_member.country = req['country']
        model_member.avatarUrl = req['avatarUrl']
        model_member.add_update()

        model_bind = OauthMemberBind()
        model_bind.member_id = model_member.id
        model_bind.type = 1
        model_bind.openid = openid
        model_bind.add_update()

    # current_app.logger.info(rjson['openid'])

    return jsonify(result)
