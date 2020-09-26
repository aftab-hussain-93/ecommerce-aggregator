from flask import render_template, Blueprint, flash, session, request, current_app
from app import db
from app.models import Items, Watchlist
from app.posts.utils import get_search_results
import random

post = Blueprint('post',__name__)

@post.route('/search/<string:category_name>/<string:search_string>')
def search(category_name,search_string):
	"""
		Checks if the search string is present in database. Displays the results off the database if presents, else scrapes the data off the website and adds to database.
	"""
	search_string = search_string.lower().strip()
	result = get_search_results(search_string)
	current_app.logger.info(f"Search id {result.id}")
	all_results = result.items
	random.shuffle(all_results)
	return render_template('search.html',results = all_results,search_str=search_string, search_id = result.id)

# @post.route('/add_to_watchlist',methods=['POST'])
# def watch():
# 	item_id, user_id, desired_price = [request.json[k] for k in ('item_id', 'user_id' , 'desired_price')]
# 	print(f"User ID {user_id}")
# 	print(f"Session User ID {session['user_id']}")
# 	try:
# 		if int(user_id) != int(session['user_id']):
# 			raise AttributeError("User ID does not match")
# 		item = Items.query.filter(Items.id == item_id).first()
# 		wc = Watchlist.query.filter_by(item_id = item.id, user_id = user_id).first()
# 		if wc:
# 			wc.desired_price = desired_price
# 		else:
# 			watch_item = Watchlist(item_id = item.id, user_id = user_id, desired_price = desired_price)
# 			db.session.add(watch_item)
# 		db.session.commit()
# 		return {"message": "successfully added"}, 201
# 	except Exception as e:
# 		current_app.logger.info("Exception - {}".format(e))
# 		return {"error": "Errored out"}, 400

@post.route('/add_to_watchlist',methods=['POST'])
def watch():
	# item_id, user_id, desired_price = [request.json[k] for k in ('item_id', 'user_id' , 'desired_price')]
	item_id = 1
	# Add item to tracked items table and scrape the current price.
	get_item_price()