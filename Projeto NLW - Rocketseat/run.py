from src.main.server.server import app

if __name__ == "__main__": #Isto é usado ao executar o servidor de forma independente 
    app.run(host='0.0.0.0', port=3000, debug=True) #modo debug