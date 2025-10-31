#!/usr/bin/env bash
set -e

echo "🚀 BitacoraFit Bootstrap"

# Check for Django
if ! python -c "import django" 2>/dev/null; then
    echo "❌ Django not found. Run 'make setup' first."
    exit 1
fi

cd src

# Create Django project
echo "📦 Creating Django project..."
django-admin startproject config .

# Create logs app
echo "📦 Creating logs app..."
python manage.py startapp logs apps/logs

echo "✅ Bootstrap complete!"
echo ""
echo "Next steps:"
echo "  1. Add config.settings to src/config/"
echo "  2. Register 'apps.logs' in INSTALLED_APPS"
echo "  3. Run 'make migrate'"
