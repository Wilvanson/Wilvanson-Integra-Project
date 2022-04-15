FROM node:12 AS build-stage

WORKDIR /my-app
COPY my-app/. .

# You have to set this because it should be set during build time.
ENV REACT_APP_BASE_URL=https://integra-project-data.herokuapp.com/

# Build our React App
RUN npm install
RUN npm run build

FROM python:3.9

# Setup Flask environment
# ENV FLASK_APP=app
# ENV FLASK_ENV=production
# ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

WORKDIR /var/www
COPY . .
COPY --from=build-stage /my-app/build/* app/static/

# Install Python Dependencies
RUN pip install -r requirements.txt

# Run flask environment
CMD gunicorn app:app