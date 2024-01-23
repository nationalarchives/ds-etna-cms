FROM ghcr.io/nationalarchives/tna-python-django:latest

# Copy in the application code
COPY --chown=app . .

# Install the dependencies
RUN tna-build

# Run the application
CMD ["tna-run", "app.wsgi.production"]