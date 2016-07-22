from flask import Flask
app=Flask("deepu")
@app.route('/')
def hello():
    return 'welcome'
app.run()