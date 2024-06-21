FROM odoo:16.0

# Set environment variables
ENV HOST=0.0.0.0 \
  PORT=8069

# Expose port for Odoo
EXPOSE 8069

# Command to start Odoo
CMD ["odoo"]