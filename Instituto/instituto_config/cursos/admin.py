from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # Columnas en el listado: Nombre, Precio y Estado
    list_display = ('nombre', 'precio', 'activo')
    
    # Filtro lateral para activos/inactivos
    list_filter = ('activo',)
    
    # Buscador por nombre
    search_fields = ('nombre',)