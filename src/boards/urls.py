from django.urls import path
from . import views as v
from files import views as v2
from financial_system import views as v3

app_name = 'boards'

urlpatterns = [
    path("boards/newboard/", 
        v.new_board, 
        name="new_board"),

    path("files/upload/", 
        v2.home, 
        name="file"),

    path('files/uploadfile/',
        v2.uploadfile,
        name="uploadfile"),

    path('files/deleteFile/<int:id>',
        v2.deleteFile,
        name="deletefile"),

    path('financial_system/stocks/',
        v3.StocksListView.as_view(),
        name='stocks'),

    path('financial_system/stocks/stock_transaction/<int:id>',
        v3.stock_transaction,
        name="stock_transaction"),

    path('financial_system/properties/',
        v3.PropertiesListView.as_view(),
        name='properties'),

    path("financial_system/properties/new_property/", 
        v3.new_property, 
        name="new_property"),

    path('financial_system/bonds/',
        v3.BondsListView.as_view(),
        name='bonds'),

    path("financial_system/bonds/new_bond/", 
        v3.new_bond, 
        name="new_bond"),

    path('financial_system/properties/property_transaction/<int:id>',
        v3.property_transaction,
        name="property_transaction"),

    path('financial_system/misc_products/',
        v3.MiscListView.as_view(),
        name='misc_products'),

    path("financial_system/misc_products/new_misc_product/", 
        v3.new_misc_product, 
        name="new_misc_product"),

    path('financial_system/misc_products/other_transaction/<int:id>',
        v3.other_transaction,
        name="other_transaction"),

    path("financial_system/user_transactions_form/", 
        v3.user_transactions_form, 
        name="user_transactions_form"),

    path("financial_system/user_transactions_form/list_user_transactions/", 
        v3.list_user_transactions, 
        name="list_user_transactions"),

    path("financial_system/stock_date_form/", 
        v3.stock_date_form, 
        name="stock_date_form"),

    path("financial_system/stock_date_form/list_stocks_on_date/", 
        v3.list_stocks_on_date, 
        name="list_stocks_on_date"),

    path("financial_system/property_data_form/", 
        v3.property_data_form, 
        name="property_data_form"),

    path("financial_system/property_data_form/list_property_data/", 
        v3.list_property_data, 
        name="list_property_data"),

    path("financial_system/bond_data_form/", 
        v3.bond_data_form, 
        name="bond_data_form"),

    path("financial_system/bond_data_form/list_bond_data/", 
        v3.list_bond_data, 
        name="list_bond_data"),

    path("financial_system/agent_assets_form/", 
        v3.agent_assets_form, 
        name="agent_assets_form"),

    path("financial_system/agent_assets_form/list_agent_assets/", 
        v3.list_agent_assets, 
        name="list_agent_assets"),

    path("financial_system/loan_ratings_form/", 
        v3.loan_ratings_form, 
        name="loan_ratings_form"),

    path("financial_system/loan_ratings_form/list_loan_ratings/", 
        v3.list_loan_ratings, 
        name="list_loan_ratings"),

    path('',
        v.BoardListView.as_view(),
        name='board_index'),

    path('boards/<str:pk>/',
        v.BoardTopicsListView.as_view(),
        name='board_topics'),

    path('boards/<str:pk>/new/topic',
    	v.new_topic,
    	name='new_topic'),

    path('boards/<str:board_pk>/topics/<str:topic_pk>/',
        v.TopicPostListView.as_view(),
        name='topic_posts'),


    path('boards/<str:board_pk>/topics/<str:topic_pk>/reply/',
    	v.reply_topic,
    	name='reply_topic'),

    path('boards/<str:board_pk>/topics/<str:topic_pk>/posts/<str:post_pk>/edit/',
    	v.PostUpdateView.as_view(),
    	name='update_post'),

]
