from api import login

if __name__ == "__main__":
    config_file = "config.json"
    token = login(config_file)
    if token:
        print("Login exitoso.")
    else:
        print("Login fallido.")
