import os
from flask import render_template, jsonify, request, session, redirect, url_for
from ams.models import User, Listing, Marks
from configure import LOGS_PATH
from . import ams, db


@ams.before_request
def verify_login(*args, **kwargs):

    if request.path.strip('/') == 'login': return None
    if request.path.strip('/') == 'assets/css/layui.css': return None
    if session.get('user_id'): return None

    return redirect(url_for('ams.login'))


@ams.route('/logdel')
def logdel():
    trace = LOGS_PATH + "/trace.txt"
    other = LOGS_PATH + "/other.txt"

    # 判断文件是否存在
    if (os.path.exists(trace)):
        with open(trace, "r+") as f:
            f.truncate()

    if (os.path.exists(other)):
        with open(other, "r+") as f:
            f.truncate()

    # if (os.path.exists(other)):
    #     os.remove(other)

    return redirect(url_for('ams.index'))


#
@ams.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.name == username, User.pwd == password).first()

        if user != None:
            session['user_id'] = user.id

            return redirect(url_for('ams.index'))

    if request.args.get('s') == '1':
        session.pop('user_id', None)

    if session.get('user_id'): return redirect(url_for('ams.index'))

    title = '登陆'
    return render_template('login.html', title=title)


#
@ams.route('/')
def index():
    title = '首页'

    curr = int(request.args.get('page')) if request.args.get('page') else 0

    ssub = db.session.query(Marks, db.func.max(Marks.uptime).label('sss')).group_by(Marks.asin_id).subquery()

    data = db.session.query((Listing.id).label('aid'), Listing.img, Listing.asin, Listing.adtime, ssub).join(ssub,
                                                                                                             isouter=True).order_by(
        Listing.adtime.desc()).limit(20).offset((curr-1)*20).all()


    coun = db.session.query(db.func.count(Listing.asin).label('count')).one()

    ss = {'title': title, 'data': data, 'curr': curr, 'count': coun[0]}

    return render_template('index.html', **ss)


#
@ams.route('/add', methods=['GET', 'POST'])
def add():

    # user = User(name='admin',pwd='1111')
    # db.session.add(user)
    # db.session.commit()

    if request.method == 'POST':

        asins = str(request.form.get('asins')).split('\n')
        asins = [tuple(i.strip().split('|')) for i in asins if i.strip() != '']
        asins = list(set(asins))

        rowss = []
        for row in asins:

            seller = row[1] if len(row) > 1 else ''

            if Listing.query.filter(Listing.asin == row[0], Listing.seller == seller).first():
                rowss.append(row)
                continue

            listing = Listing(asin=row[0], seller=seller, user_id=session.get('user_id'))

            db.session.add(listing)

        db.session.commit()

        return jsonify(rowss)

    title = '添加ASIN'
    return render_template('add.html', title=title)


#
@ams.route('/lists')
def lists():

    id = request.args.get('id')

    if id.isdigit() and int(id) > 0:
        data = db.session.query(Marks).filter(Marks.asin_id == id).order_by(Marks.asin_id.desc()).all()
    else:

        data = db.session.query(Marks).order_by(Marks.asin_id.desc()).all()

    title = '全部数据'

    return render_template('lists.html', title=title, data=data)


#
@ams.route('/export/<int:id>')
def export(id):
    from flask import make_response

    import tablib

    if id > 0:

        res = db.session.query(Marks).filter(Marks.asin_id == id).all()
    else:
        res = db.session.query(Marks).all()

    head = (u"ASIN", u"类目排名", u"价格", u"库存", u"查询时间")

    info = [(i.listing.asin, i.bsr, i.price, i.stock, i.uptime.strftime("%Y-%m-%d %H:%M:%S")) for i in res]

    data = tablib.Dataset(*info, headers=head)

    resp = make_response(data.xls)

    filename = 'amazon.xls'  # 用户下载默认文件名

    resp.headers["Content-Disposition"] = "attachment; filename=" + filename  # 指定响应为下载文件

    resp.headers['Content-Type'] = 'xls'  # 不指定的话会默认下载html格式，下载后还要改格式才能看

    return resp


#
@ams.route('/del/<int:id>')
def delasin(id):
    db.session.query(Listing).filter(Listing.id == id).delete()
    db.session.query(Marks).filter(Marks.asin_id == id).delete()

    db.session.commit()

    return redirect(url_for('ams.index'))


@ams.route('/drop')
def drop():

    db.drop_all()

    db.create_all()

    user = User(name='admin',pwd='11111')

    db.session.add(user)

    db.session.commit()

    return redirect(url_for('ams.add'))


@ams.route('/test')
def test():
    return render_template('a1.html')
