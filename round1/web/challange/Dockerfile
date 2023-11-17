# Use an official Nginx runtime as a parent image
FROM nginx:latest

# Set the working directory to /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

# Copy the index.html and robots.txt files into the container
COPY index.html .
COPY robots.txt .
COPY flag.html .
COPY banana .

# Make port 80 available to the world outside this container
EXPOSE 80
