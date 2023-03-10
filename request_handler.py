from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_single_post, get_all_posts, create_post, get_all_posts_by_user, get_all_posts_by_title, delete_post, update_post
from views import get_all_users, get_single_user, get_user_by_username
from views import get_all_comments_by_post
from views import create_user, login_user
from views import get_all_comments_by_post, get_all_comments, get_single_comment, create_comment, delete_comment
from views import get_single_category, get_all_categories



class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    # def parse_url(self, path):
    #     """Parse the url into the resource and id"""
    #     parsed_url = urlparse(path)
    #     path_params = self.path.split('/')
    #     resource = path_params[1]

    #     if parsed_url.query:
    #         query = parse_qs(parsed_url.query)
    #         return (resource, query)
        
    #     if '?' in resource:
    #         param = resource.split('?')[1]
    #         resource = resource.split('?')[0]
    #         pair = param.split('=')
    #         key = pair[0]
    #         value = pair[1]
    #         return (resource, key, value)
    #     else:
    #         id = None
    #         try:
    #             id = int(path_params[2])
    #         except (IndexError, ValueError):
    #             pass
    #         return (resource, id)

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/') 
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        
        """Handle Get requests to the server"""

        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                    self._set_headers(200)
                else:
                    self._set_headers(200)
                    response = get_all_posts()

            elif resource == "users":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_user(id)
                
                else:
                    self._set_headers(200)
                    response = get_all_users()

            elif resource == "comments":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_comment(id)
                
                else:
                    self._set_headers(200)
                    response = get_all_comments()

            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)
                    self._set_headers(200)
                else:
                    self._set_headers(200)
                    response = get_all_categories()

        else:  # There is a ? in the path, run the query param functions
            (resource, query) = parsed

            if query.get('username') and resource == 'users':
                self._set_headers(200)
                response = get_user_by_username(query['username'][0])

            elif query.get('post_id') and resource == 'comments':
                self._set_headers(200)
                response = get_all_comments_by_post(query['post_id'][0])
            
            elif query.get('title') and resource == 'posts':
                self._set_headers(200)
                response = get_all_posts_by_title(query['title'][0])

            elif query.get('user_id') and resource == 'posts':
                self._set_headers(200)
                response = get_all_posts_by_user(query['user_id'][0])
                
                
        self.wfile.write(json.dumps(response).encode())

        

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, id) = self.parse_url(self.path)

        new_post = None
        new_comment = None
        
        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
            
        if resource == 'posts':
            response = create_post(post_body)
        if resource == 'comments':
            response = create_comment(post_body)

        self.wfile.write(json.dumps(response).encode())
        

    def do_PUT(self):
        """Handles PUT requests to the server"""
    
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        success = False
        if resource == "posts":
            success = update_post(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "posts":
            delete_post(id)

        if resource == "comments":
            delete_comment(id)

        self.wfile.write("".encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
