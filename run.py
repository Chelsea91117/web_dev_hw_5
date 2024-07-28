from app import create_app, drop_all_tables

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)