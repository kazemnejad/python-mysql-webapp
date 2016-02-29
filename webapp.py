import os
from jinja2 import Environment, FileSystemLoader
from mysql.connector import MySQLConnection
from werkzeug.routing import Map, Rule

from helpers import HtmlRenderHelper


class AwesomeWeblog(object):
    def __init__(self):
        # Initializing template engine
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)

    def get_urls(self):
        return Map([
            Rule('/', endpoint='get_main_page'),
            Rule('/show-post/<post_id>', endpoint='show_post'),
        ])

    def get_main_page(self, request):
        db = MySQLConnection(
                host="localhost",
                user="root",
                password="12345",
                database="test",
                autocommit=True
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM posts ORDER BY id LIMIT 9")
        posts = cursor.fetchall()

        db.close()

        return HtmlRenderHelper.render_main_page(self.jinja_env, posts=posts)

    def show_post(self, request, **args):
        # get post_id from url, eg: http://127.0.0.1:5000/show-post/5
        postId = args.get("post_id")

        # establish a connection to MySQL server
        db = MySQLConnection(
                host="localhost",
                user="root",
                password="12345",
                database="test",
                autocommit=True
        )

        # get SQL executor from db connection
        cursor = db.cursor()

        # send query to MySQL server to get the post
        cursor.execute("SELECT * FROM posts WHERE id = " + postId)

        # receive the results
        post = cursor.fetchone()

        # show error to user if there wasn't any matched data in database
        if post is None:
            return "Not Found"

        result = ""
        result += "id: " + str(post[0])
        result += "<br>"
        result += "title: " + post[1]
        result += "<br>"
        result += "body: " + post[3]
        result += "<br>"

        # send another query to get comments for this post
        cursor.execute("SELECT * FROM comments WHERE post_id = " + postId)
        comments = cursor.fetchall()
        for comment in comments:
            result += "<br>"
            result += "Comment body: " + comment[1]
            result += "<br>"

        db.close()
        return str(result)
