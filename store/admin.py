from django.contrib import admin
from .models import Product, Collection


# Register your models here.



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
      list_display = ['title','price', 'description', "inventory"]
      list_per_page = 10
      list_editable = ['price', 'description']
      search_fields = ['title']

      @admin.display(ordering='inventory')
      def inventory_status(self, production: Product):
        if production.inventory < 20:
              return "Low"
        return "Ok"

      @admin.register(Collection)
      class CollectionAdmin(admin.ModelAdmin):
          list_display = ['id','title','production_count']
          list_per_page = 10

          @admin.display(ordering='production_count')
          def production_count(self,collection:Collection):
              return collection.product_set.count()



      # class Meta:
      #       ordering = ['title']
