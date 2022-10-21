from livereload import Server, shell

if __name__ == '__main__':
    server = Server()
    server.watch('src/*.rst', shell('make html'), delay=1)
    server.watch('src/*.md', shell('make html'), delay=1)
    server.watch('src/*.py', shell('make html'), delay=1)
    server.watch('_static/*', shell('make html'), delay=1)
    server.watch('_templates/*', shell('make html'), delay=1)
    server.serve(root='docs/html')