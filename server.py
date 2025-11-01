#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # URL routing for clean URLs
        url_map = {
            '/': '/index.html',
            '/home': '/index.html',
            '/about': '/about.html',
            '/service': '/service.html',
            '/services': '/service.html',
            '/booking': '/booking.html',
            '/testimonial': '/testimonial.html',
            '/testimonials': '/testimonial.html',
            '/contact': '/contact.html',
            '/404': '/404.html'
        }
        
        # Map clean URLs to actual files
        if self.path in url_map:
            self.path = url_map[self.path]
        
        # If path doesn't have extension and isn't in map, try adding .html
        elif '.' not in os.path.basename(self.path.split('?')[0]) and self.path != '/':
            path_clean = self.path.split('?')[0].lstrip('/')
            if path_clean:  # Only if there's a path component
                potential_file = '/' + path_clean + '.html'
                if os.path.exists(path_clean + '.html'):
                    query_string = '?' + self.path.split('?')[1] if '?' in self.path else ''
                    self.path = potential_file + query_string
        
        return super().do_GET()

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Serving directory: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

