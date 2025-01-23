from datetime import datetime
"""
Context processors for handle current year in the copyright block.
"""
def current_year(request):
    return {
        'current_year': datetime.now().year,
    }