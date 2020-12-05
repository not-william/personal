FROM node:latest as build-stage
WORKDIR /app
COPY package.json ./
RUN npm cache clean --force
RUN npm install
CMD npm run build
