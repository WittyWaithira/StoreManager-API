from app import create_appapi

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
