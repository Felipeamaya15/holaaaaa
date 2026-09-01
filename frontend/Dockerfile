FROM node:20-alpine

WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias si existe package.json, o continuar
RUN npm install || true

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]