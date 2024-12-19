#Fields of model: product.template

#Field: website_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|Restrict to a specific website.|

|manual|False|

|name|website_id|

|readonly|False|

|relation|website|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website|

|type|many2one|

#Field: website_published

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['is_published', 'website_id']|

|exportable|True|

|groupable|False|

|manual|False|

|name|website_published|

|readonly|False|

|related|False|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Visible on current website|

|type|boolean|

#Field: is_published

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|is_published|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Is Published|

|type|boolean|

#Field: can_publish

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|can_publish|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Can Publish|

|type|boolean|

#Field: website_url

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|The full URL to access the document through the website.|

|manual|False|

|name|website_url|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Website URL|

|translate|False|

|trim|True|

|type|char|

#Field: is_seo_optimized

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|is_seo_optimized|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|SEO optimized|

|type|boolean|

#Field: website_meta_title

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_meta_title|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website meta title|

|translate|True|

|trim|True|

|type|char|

#Field: website_meta_description

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_meta_description|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website meta description|

|translate|True|

|type|text|

#Field: website_meta_keywords

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_meta_keywords|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website meta keywords|

|translate|True|

|trim|True|

|type|char|

#Field: website_meta_og_img

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_meta_og_img|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website opengraph image|

|translate|False|

|trim|True|

|type|char|

#Field: seo_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|seo_name|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Seo name|

|translate|True|

|trim|True|

|type|char|

#Field: image_1920

|attachment|True|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|image_1920|

|readonly|False|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Image|

|type|binary|

#Field: image_1024

|attachment|True|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['image_1920']|

|exportable|True|

|groupable|False|

|manual|False|

|name|image_1024|

|readonly|True|

|related|image_1920|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Image 1024|

|type|binary|

#Field: image_512

|attachment|True|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['image_1920']|

|exportable|True|

|groupable|False|

|manual|False|

|name|image_512|

|readonly|True|

|related|image_1920|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Image 512|

|type|binary|

#Field: image_256

|attachment|True|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['image_1920']|

|exportable|True|

|groupable|False|

|manual|False|

|name|image_256|

|readonly|True|

|related|image_1920|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Image 256|

|type|binary|

#Field: image_128

|attachment|True|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['image_1920']|

|exportable|True|

|groupable|False|

|manual|False|

|name|image_128|

|readonly|True|

|related|image_1920|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Image 128|

|type|binary|

#Field: activity_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_ids|

|readonly|False|

|relation|mail.activity|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Activities|

|type|one2many|

#Field: activity_state

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.state']|

|exportable|True|

|groupable|True|

|groups|base.group_user|

|help|Status based on activities
Overdue: Due date is already passed
Today: Activity date is today
Planned: Future activities.|

|manual|False|

|name|activity_state|

|readonly|True|

|required|False|

|searchable|True|

|selection|[['overdue', 'Overdue'], ['today', 'Today'], ['planned', 'Planned']]|

|sortable|False|

|store|False|

|string|Activity State|

|type|selection|

#Field: activity_user_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['activity_ids.user_id']|

|domain|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_user_id|

|readonly|True|

|relation|res.users|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Responsible User|

|type|many2one|

#Field: activity_type_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['activity_ids.activity_type_id']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_type_id|

|readonly|False|

|related|activity_ids.activity_type_id|

|relation|mail.activity.type|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Next Activity Type|

|type|many2one|

#Field: activity_type_icon

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.icon']|

|exportable|True|

|groupable|False|

|help|Font awesome icon e.g. fa-tasks|

|manual|False|

|name|activity_type_icon|

|readonly|True|

|related|activity_ids.icon|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Activity Type Icon|

|translate|False|

|trim|True|

|type|char|

#Field: activity_date_deadline

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.date_deadline']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_date_deadline|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Next Activity Deadline|

|type|date|

#Field: my_activity_date_deadline

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.date_deadline', 'activity_ids.user_id']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|my_activity_date_deadline|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|My Activity Deadline|

|type|date|

#Field: activity_summary

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.summary']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_summary|

|readonly|False|

|related|activity_ids.summary|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Next Activity Summary|

|translate|False|

|trim|True|

|type|char|

#Field: activity_exception_decoration

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.activity_type_id.decoration_type', 'activity_ids.activity_type_id.icon']|

|exportable|True|

|groupable|False|

|help|Type of the exception activity on record.|

|manual|False|

|name|activity_exception_decoration|

|readonly|True|

|required|False|

|searchable|True|

|selection|[['warning', 'Alert'], ['danger', 'Error']]|

|sortable|False|

|store|False|

|string|Activity Exception Decoration|

|type|selection|

#Field: activity_exception_icon

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['activity_ids.activity_type_id.decoration_type', 'activity_ids.activity_type_id.icon']|

|exportable|True|

|groupable|False|

|help|Icon to indicate an exception activity.|

|manual|False|

|name|activity_exception_icon|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Icon|

|translate|False|

|trim|True|

|type|char|

#Field: activity_calendar_event_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['activity_ids.calendar_event_id']|

|domain|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|activity_calendar_event_id|

|readonly|True|

|relation|calendar.event|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Next Activity Calendar Event|

|type|many2one|

#Field: message_is_follower

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['message_follower_ids']|

|exportable|True|

|groupable|False|

|manual|False|

|name|message_is_follower|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Is Follower|

|type|boolean|

#Field: message_follower_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|message_follower_ids|

|readonly|False|

|relation|mail.followers|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Followers|

|type|one2many|

#Field: message_partner_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['message_follower_ids']|

|domain|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|message_partner_ids|

|readonly|False|

|relation|res.partner|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Followers (Partners)|

|type|many2many|

#Field: message_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[['message_type', '!=', 'user_notification']]|

|exportable|True|

|groupable|False|

|manual|False|

|name|message_ids|

|readonly|False|

|relation|mail.message|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Messages|

|type|one2many|

#Field: has_message

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|has_message|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Has Message|

|type|boolean|

#Field: message_needaction

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|If checked, new messages require your attention.|

|manual|False|

|name|message_needaction|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Action Needed|

|type|boolean|

#Field: message_needaction_counter

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|Number of messages requiring action|

|manual|False|

|name|message_needaction_counter|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Number of Actions|

|type|integer|

#Field: message_has_error

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|If checked, some messages have a delivery error.|

|manual|False|

|name|message_has_error|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Message Delivery error|

|type|boolean|

#Field: message_has_error_counter

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|Number of messages with delivery error|

|manual|False|

|name|message_has_error_counter|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Number of errors|

|type|integer|

#Field: message_attachment_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|message_attachment_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Attachment Count|

|type|integer|

#Field: rating_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[['res_model', '=', 'product.template']]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_ids|

|readonly|False|

|relation|rating.rating|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Ratings|

|type|one2many|

#Field: website_message_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[['model', '=', 'product.template'], ['message_type', 'in', ['comment', 'email', 'email_outgoing']]]|

|exportable|True|

|groupable|False|

|help|Website communication history|

|manual|False|

|name|website_message_ids|

|readonly|False|

|relation|mail.message|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Website Messages|

|type|one2many|

#Field: message_has_sms_error

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|If checked, some messages have a delivery error.|

|manual|False|

|name|message_has_sms_error|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|SMS Delivery error|

|type|boolean|

#Field: name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|name|

|readonly|False|

|required|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Name|

|translate|True|

|trim|True|

|type|char|

#Field: sequence

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Gives the sequence order when displaying a product list|

|manual|False|

|name|sequence|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Sequence|

|type|integer|

#Field: description

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description|

|readonly|False|

|required|False|

|sanitize|True|

|sanitize_attributes|True|

|sanitize_style|False|

|sanitize_tags|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Description|

|strip_classes|False|

|strip_style|False|

|translate|True|

|type|html|

#Field: description_purchase

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description_purchase|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Purchase Description|

|translate|True|

|type|text|

#Field: description_sale

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|A description of the Product that you want to communicate to your customers. This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note|

|manual|False|

|name|description_sale|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Sales Description|

|translate|True|

|type|text|

#Field: type

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Goods are tangible materials and merchandise you provide.
A service is a non-material product you provide.|

|manual|False|

|name|type|

|readonly|False|

|required|True|

|searchable|True|

|selection|[['consu', 'Goods'], ['service', 'Service'], ['combo', 'Combo']]|

|sortable|True|

|store|True|

|string|Product Type|

|type|selection|

#Field: combo_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|(company_id and [('company_id', 'in', [company_id] + [False])] or [('company_id', '=', False)]) + ([])|

|exportable|True|

|groupable|True|

|manual|False|

|name|combo_ids|

|readonly|False|

|relation|product.combo|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Combo Choices|

|type|many2many|

#Field: service_tracking

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['sale_ok', 'type']|

|exportable|True|

|groupable|True|

|manual|False|

|name|service_tracking|

|readonly|False|

|required|True|

|searchable|True|

|selection|[['no', 'Nothing'], ['event', 'Event Registration']]|

|sortable|True|

|store|True|

|string|Create on Order|

|type|selection|

#Field: categ_id

|change_default|True|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|categ_id|

|readonly|False|

|relation|product.category|

|required|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Product Category|

|type|many2one|

#Field: currency_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['company_id']|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|currency_id|

|readonly|True|

|relation|res.currency|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Currency|

|type|many2one|

#Field: cost_currency_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['company_id']|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|cost_currency_id|

|readonly|True|

|relation|res.currency|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Cost Currency|

|type|many2one|

#Field: list_price

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|digits|[16, 2]|

|exportable|True|

|groupable|True|

|help|Price at which the product is sold to customers.|

|manual|False|

|name|list_price|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Sales Price|

|type|float|

#Field: standard_price

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.standard_price']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|help|Value of the product (automatically computed in AVCO).
        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
        Used to compute margins on sale orders.|

|manual|False|

|name|standard_price|

|readonly|False|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Cost|

|type|float|

#Field: volume

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.volume']|

|digits|[16, 2]|

|exportable|True|

|groupable|True|

|manual|False|

|name|volume|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Volume|

|type|float|

#Field: volume_uom_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type']|

|exportable|True|

|groupable|False|

|manual|False|

|name|volume_uom_name|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Volume unit of measure label|

|translate|False|

|trim|True|

|type|char|

#Field: weight

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.weight']|

|digits|[16, 2]|

|exportable|True|

|groupable|True|

|manual|False|

|name|weight|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Weight|

|type|float|

#Field: weight_uom_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type']|

|exportable|True|

|groupable|False|

|manual|False|

|name|weight_uom_name|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Weight unit of measure label|

|translate|False|

|trim|True|

|type|char|

#Field: sale_ok

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|sale_ok|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Sales|

|type|boolean|

#Field: purchase_ok

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|purchase_ok|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Purchase|

|type|boolean|

#Field: uom_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|Default unit of measure used for all stock operations.|

|manual|False|

|name|uom_id|

|readonly|False|

|relation|uom.uom|

|required|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Unit of Measure|

|type|many2one|

#Field: uom_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['uom_id.name']|

|exportable|True|

|groupable|True|

|manual|False|

|name|uom_name|

|readonly|True|

|related|uom_id.name|

|required|False|

|searchable|True|

|sortable|True|

|store|False|

|string|Unit of Measure Name|

|translate|True|

|trim|True|

|type|char|

#Field: uom_po_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['uom_id']|

|domain|[]|

|exportable|True|

|groupable|True|

|help|Default unit of measure used for purchase orders. It must be in the same category as the default unit of measure.|

|manual|False|

|name|uom_po_id|

|readonly|False|

|relation|uom.uom|

|required|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Purchase Unit|

|type|many2one|

#Field: company_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|company_id|

|readonly|False|

|relation|res.company|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Company|

|type|many2one|

#Field: packaging_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['product_variant_ids', 'product_variant_ids.packaging_ids']|

|domain|[]|

|exportable|True|

|groupable|False|

|help|Gives the different ways to package the same product.|

|manual|False|

|name|packaging_ids|

|readonly|False|

|relation|product.packaging|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Product Packages|

|type|one2many|

#Field: seller_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|seller_ids|

|readonly|False|

|relation|product.supplierinfo|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Vendors|

|type|one2many|

#Field: variant_seller_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|variant_seller_ids|

|readonly|False|

|relation|product.supplierinfo|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Variant Seller|

|type|one2many|

#Field: active

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|If unchecked, it will allow you to hide the product without removing it.|

|manual|False|

|name|active|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Active|

|type|boolean|

#Field: color

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|color|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Color Index|

|type|integer|

#Field: is_product_variant

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|is_product_variant|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Is a product variant|

|type|boolean|

#Field: attribute_line_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|attribute_line_ids|

|readonly|False|

|relation|product.template.attribute.line|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Product Attributes|

|type|one2many|

#Field: valid_product_template_attribute_line_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['attribute_line_ids.value_ids']|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|valid_product_template_attribute_line_ids|

|readonly|True|

|relation|product.template.attribute.line|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Valid Product Attribute Lines|

|type|many2many|

#Field: product_variant_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_variant_ids|

|readonly|False|

|relation|product.product|

|relation_field|product_tmpl_id|

|required|True|

|searchable|True|

|sortable|False|

|store|True|

|string|Products|

|type|one2many|

#Field: product_variant_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['product_variant_ids']|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_variant_id|

|readonly|True|

|relation|product.product|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Product|

|type|many2one|

#Field: product_variant_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.product_tmpl_id']|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_variant_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|# Product Variants|

|type|integer|

#Field: barcode

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.barcode']|

|exportable|True|

|groupable|False|

|manual|False|

|name|barcode|

|readonly|False|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Barcode|

|translate|False|

|trim|True|

|type|char|

#Field: default_code

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.default_code']|

|exportable|True|

|groupable|True|

|manual|False|

|name|default_code|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Internal Reference|

|translate|False|

|trim|True|

|type|char|

#Field: pricelist_item_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|pricelist_item_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Number of price rules|

|type|integer|

#Field: product_document_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[['res_model', '=', 'product.template']]|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_document_ids|

|readonly|False|

|relation|product.document|

|relation_field|res_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Documents|

|type|one2many|

#Field: product_document_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_document_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Documents Count|

|type|integer|

#Field: can_image_1024_be_zoomed

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['image_1920', 'image_1024']|

|exportable|True|

|groupable|True|

|manual|False|

|name|can_image_1024_be_zoomed|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Can Image 1024 be zoomed|

|type|boolean|

#Field: has_configurable_attributes

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['attribute_line_ids', 'attribute_line_ids.value_ids', 'attribute_line_ids.attribute_id.create_variant', 'attribute_line_ids.attribute_id.display_type', 'attribute_line_ids.value_ids.is_custom']|

|exportable|True|

|groupable|True|

|manual|False|

|name|has_configurable_attributes|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Is a configurable product|

|type|boolean|

#Field: product_tooltip

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['invoice_policy', 'sale_ok', 'service_tracking', 'type']|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_tooltip|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Product Tooltip|

|translate|False|

|trim|True|

|type|char|

#Field: is_favorite

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|is_favorite|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Favorite|

|type|boolean|

#Field: product_tag_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|product_tag_ids|

|readonly|False|

|relation|product.tag|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Tags|

|type|many2many|

#Field: product_properties

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|definition_record|categ_id|

|definition_record_field|product_properties_definition|

|depends|['categ_id']|

|exportable|True|

|groupable|True|

|manual|False|

|name|product_properties|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Properties|

|type|properties|

#Field: id

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|id|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|ID|

|type|integer|

#Field: display_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['name', 'default_code', 'name']|

|exportable|True|

|groupable|False|

|manual|False|

|name|display_name|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Display Name|

|translate|False|

|trim|True|

|type|char|

#Field: create_uid

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|create_uid|

|readonly|True|

|relation|res.users|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Created by|

|type|many2one|

#Field: create_date

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|create_date|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Created on|

|type|datetime|

#Field: write_uid

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|write_uid|

|readonly|True|

|relation|res.users|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Last Updated by|

|type|many2one|

#Field: write_date

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|write_date|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Last Updated on|

|type|datetime|

#Field: taxes_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['taxes_id.type_tax_use']|

|domain|[['type_tax_use', '=', 'sale']]|

|exportable|True|

|groupable|True|

|help|Default taxes used when selling the product|

|manual|False|

|name|taxes_id|

|readonly|False|

|relation|account.tax|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Sales Taxes|

|type|many2many|

#Field: tax_string

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['taxes_id', 'list_price']|

|exportable|True|

|groupable|False|

|manual|False|

|name|tax_string|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Tax String|

|translate|False|

|trim|True|

|type|char|

#Field: supplier_taxes_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['supplier_taxes_id.type_tax_use']|

|domain|[['type_tax_use', '=', 'purchase']]|

|exportable|True|

|groupable|True|

|help|Default taxes used when buying the product|

|manual|False|

|name|supplier_taxes_id|

|readonly|False|

|relation|account.tax|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Purchase Taxes|

|type|many2many|

#Field: property_account_income_id

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|['&', ('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable','liability_payable','asset_cash','liability_credit_card','off_balance'))]|

|exportable|True|

|groupable|True|

|help|Keep this field empty to use the default value from the product category.|

|manual|False|

|name|property_account_income_id|

|readonly|False|

|relation|account.account|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Income Account|

|type|many2one|

#Field: property_account_expense_id

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|['&', ('deprecated', '=', False), ('account_type', 'not in', ('asset_receivable','liability_payable','asset_cash','liability_credit_card','off_balance'))]|

|exportable|True|

|groupable|True|

|help|Keep this field empty to use the default value from the product category. If anglo-saxon accounting with automated valuation method is configured, the expense account on the product category will be used.|

|manual|False|

|name|property_account_expense_id|

|readonly|False|

|relation|account.account|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Expense Account|

|type|many2one|

#Field: account_tag_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[('applicability', '=', 'products')]|

|exportable|True|

|groupable|True|

|help|Tags to be set on the base and tax journal items created for this product.|

|manual|False|

|name|account_tag_ids|

|readonly|False|

|relation|account.account.tag|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Account Tags|

|type|many2many|

#Field: fiscal_country_codes

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['company_id']|

|exportable|True|

|groupable|False|

|manual|False|

|name|fiscal_country_codes|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Fiscal Country Codes|

|translate|False|

|trim|True|

|type|char|

#Field: is_storable

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type']|

|exportable|True|

|groupable|True|

|help|A storable product is a product for which you manage stock.|

|manual|False|

|name|is_storable|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Track Inventory|

|type|boolean|

#Field: responsible_id

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[('company_ids', 'in', [allowed_company_ids[0]])] + []|

|exportable|True|

|groupable|True|

|help|This user will be responsible of the next activities related to logistic operations for this product.|

|manual|False|

|name|responsible_id|

|readonly|False|

|relation|res.users|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Responsible|

|type|many2one|

#Field: property_stock_production

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[('company_id', 'in', [allowed_company_ids[0]] + [False])] + [('usage', '=', 'production'), '|', ('company_id', '=', False), ('company_id', '=', allowed_company_ids[0])]|

|exportable|True|

|groupable|True|

|help|This stock location will be used, instead of the default one, as the source location for stock moves generated by manufacturing orders.|

|manual|False|

|name|property_stock_production|

|readonly|False|

|relation|stock.location|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Production Location|

|type|many2one|

#Field: property_stock_inventory

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[('company_id', 'in', [allowed_company_ids[0]] + [False])] + [('usage', '=', 'inventory'), '|', ('company_id', '=', False), ('company_id', '=', allowed_company_ids[0])]|

|exportable|True|

|groupable|True|

|help|This stock location will be used, instead of the default one, as the source location for stock moves generated when you do an inventory.|

|manual|False|

|name|property_stock_inventory|

|readonly|False|

|relation|stock.location|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Inventory Location|

|type|many2one|

#Field: sale_delay

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Delivery lead time, in days. It's the number of days, promised to the customer, between the confirmation of the sales order and the delivery.|

|manual|False|

|name|sale_delay|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Customer Lead Time|

|type|integer|

#Field: tracking

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['is_storable']|

|exportable|True|

|groupable|True|

|help|Ensure the traceability of a storable product in your warehouse.|

|manual|False|

|name|tracking|

|readonly|False|

|required|True|

|searchable|True|

|selection|[['serial', 'By Unique Serial Number'], ['lot', 'By Lots'], ['none', 'By Quantity']]|

|sortable|True|

|store|True|

|string|Tracking|

|type|selection|

#Field: description_picking

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description_picking|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Description on Picking|

|translate|True|

|type|text|

#Field: description_pickingout

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description_pickingout|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Description on Delivery Orders|

|translate|True|

|type|text|

#Field: description_pickingin

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description_pickingin|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Description on Receptions|

|translate|True|

|type|text|

#Field: qty_available

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.qty_available', 'product_variant_ids.virtual_available', 'product_variant_ids.incoming_qty', 'product_variant_ids.outgoing_qty']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|qty_available|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Quantity On Hand|

|type|float|

#Field: virtual_available

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.qty_available', 'product_variant_ids.virtual_available', 'product_variant_ids.incoming_qty', 'product_variant_ids.outgoing_qty']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|virtual_available|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Forecasted Quantity|

|type|float|

#Field: incoming_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.qty_available', 'product_variant_ids.virtual_available', 'product_variant_ids.incoming_qty', 'product_variant_ids.outgoing_qty']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|incoming_qty|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Incoming|

|type|float|

#Field: outgoing_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.qty_available', 'product_variant_ids.virtual_available', 'product_variant_ids.incoming_qty', 'product_variant_ids.outgoing_qty']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|outgoing_qty|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Outgoing|

|type|float|

#Field: location_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|location_id|

|readonly|False|

|relation|stock.location|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Location|

|type|many2one|

#Field: warehouse_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|warehouse_id|

|readonly|False|

|relation|stock.warehouse|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Warehouse|

|type|many2one|

#Field: has_available_route_ids

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['is_storable']|

|exportable|True|

|groupable|False|

|manual|False|

|name|has_available_route_ids|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Routes can be selected on this product|

|type|boolean|

#Field: route_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['route_ids.product_selectable']|

|domain|[['product_selectable', '=', True]]|

|exportable|True|

|groupable|True|

|help|Depending on the modules installed, this will allow you to define the route of the product: whether it will be bought, manufactured, replenished on order, etc.|

|manual|False|

|name|route_ids|

|readonly|False|

|relation|stock.route|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Routes|

|type|many2many|

#Field: nbr_moves_in

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|Number of incoming stock moves in the past 12 months|

|manual|False|

|name|nbr_moves_in|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Nbr Moves In|

|type|integer|

#Field: nbr_moves_out

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|help|Number of outgoing stock moves in the past 12 months|

|manual|False|

|name|nbr_moves_out|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Nbr Moves Out|

|type|integer|

#Field: nbr_reordering_rules

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|nbr_reordering_rules|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Reordering Rules|

|type|integer|

#Field: reordering_min_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|reordering_min_qty|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Reordering Min Qty|

|type|float|

#Field: reordering_max_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|reordering_max_qty|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Reordering Max Qty|

|type|float|

#Field: route_from_categ_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['categ_id.total_route_ids']|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|route_from_categ_ids|

|readonly|True|

|related|categ_id.total_route_ids|

|relation|stock.route|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Category Routes|

|type|many2many|

#Field: show_on_hand_qty_status_button

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['is_storable']|

|exportable|True|

|groupable|False|

|manual|False|

|name|show_on_hand_qty_status_button|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Show On Hand Qty Status Button|

|type|boolean|

#Field: show_forecasted_qty_status_button

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['is_storable']|

|exportable|True|

|groupable|False|

|manual|False|

|name|show_forecasted_qty_status_button|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Show Forecasted Qty Status Button|

|type|boolean|

#Field: bom_line_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|bom_line_ids|

|readonly|False|

|relation|mrp.bom.line|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|BoM Components|

|type|one2many|

#Field: bom_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|bom_ids|

|readonly|False|

|relation|mrp.bom|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Bill of Materials|

|type|one2many|

#Field: bom_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|bom_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|# Bill of Material|

|type|integer|

#Field: used_in_bom_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|used_in_bom_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|# of BoM Where is Used|

|type|integer|

#Field: mrp_product_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|mrp_product_qty|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Manufactured|

|type|float|

#Field: is_kits

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|is_kits|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Is Kits|

|type|boolean|

#Field: email_template_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|When validating an invoice, an email will be sent to the customer based on this template. The customer will receive an email for each product linked to an email template.|

|manual|False|

|name|email_template_id|

|readonly|False|

|relation|mail.template|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Product Email Template|

|type|many2one|

#Field: purchased_product_qty

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|purchased_product_qty|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Purchased|

|type|float|

#Field: purchase_method

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type']|

|exportable|True|

|groupable|True|

|help|On ordered quantities: Control bills based on ordered quantities.
On received quantities: Control bills based on received quantities.|

|manual|False|

|name|purchase_method|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['purchase', 'On ordered quantities'], ['receive', 'On received quantities']]|

|sortable|True|

|store|True|

|string|Control Policy|

|type|selection|

#Field: purchase_line_warn

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.|

|manual|False|

|name|purchase_line_warn|

|readonly|False|

|required|True|

|searchable|True|

|selection|[['no-message', 'No Message'], ['warning', 'Warning'], ['block', 'Blocking Message']]|

|sortable|True|

|store|True|

|string|Purchase Order Line Warning|

|type|selection|

#Field: purchase_line_warn_msg

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|purchase_line_warn_msg|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Message for Purchase Order Line|

|translate|False|

|type|text|

#Field: cost_method

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['categ_id.property_cost_method']|

|exportable|True|

|groupable|True|

|help|Standard Price: The products are valued at their standard cost defined on the product.
        Average Cost (AVCO): The products are valued at weighted average cost.
        First In First Out (FIFO): The products are valued supposing those that enter the company first will also leave it first.
        |

|manual|False|

|name|cost_method|

|readonly|True|

|related|categ_id.property_cost_method|

|required|False|

|searchable|True|

|selection|[['standard', 'Standard Price'], ['fifo', 'First In First Out (FIFO)'], ['average', 'Average Cost (AVCO)']]|

|sortable|True|

|store|False|

|string|Costing Method|

|type|selection|

#Field: valuation

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['categ_id.property_valuation']|

|exportable|True|

|groupable|True|

|help|Manual: The accounting entries to value the inventory are not posted automatically.
        Automated: An accounting entry is automatically created to value the inventory when a product enters or leaves the company.
        |

|manual|False|

|name|valuation|

|readonly|True|

|related|categ_id.property_valuation|

|required|False|

|searchable|True|

|selection|[['manual_periodic', 'Manual'], ['real_time', 'Automated']]|

|sortable|True|

|store|False|

|string|Inventory Valuation|

|type|selection|

#Field: lot_valuated

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['tracking']|

|exportable|True|

|groupable|True|

|help|If checked, the valuation will be specific by Lot/Serial number.|

|manual|False|

|name|lot_valuated|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Valuation by Lot/Serial number|

|type|boolean|

#Field: property_account_creditor_price_difference

|change_default|False|

|company_dependent|True|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|This account is used in automated inventory valuation to record the price difference between a purchase order and its related vendor bill when validating this vendor bill.|

|manual|False|

|name|property_account_creditor_price_difference|

|readonly|False|

|relation|account.account|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Price Difference Account|

|type|many2one|

#Field: service_type

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type', 'type']|

|exportable|True|

|groupable|True|

|help|Manually set quantities on order: Invoice based on the manually entered quantity, without creating an analytic account.
Timesheets on contract: Invoice based on the tracked hours on the related timesheet.
Create a task and track hours: Create a task on the sales order validation and track the work hours.|

|manual|False|

|name|service_type|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['manual', 'Manually set quantities on order']]|

|sortable|True|

|store|True|

|string|Track Service|

|type|selection|

#Field: sale_line_warn

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Selecting the "Warning" option will notify user with the message, Selecting "Blocking Message" will throw an exception with the message and block the flow. The Message has to be written in the next field.|

|manual|False|

|name|sale_line_warn|

|readonly|False|

|required|True|

|searchable|True|

|selection|[['no-message', 'No Message'], ['warning', 'Warning'], ['block', 'Blocking Message']]|

|sortable|True|

|store|True|

|string|Sales Order Line|

|type|selection|

#Field: sale_line_warn_msg

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|sale_line_warn_msg|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Message for Sales Order Line|

|translate|False|

|type|text|

#Field: expense_policy

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type', 'sale_ok']|

|exportable|True|

|groupable|True|

|help|Validated expenses, vendor bills, or stock pickings (set up to track costs) can be invoiced to the customer at either cost or sales price.|

|manual|False|

|name|expense_policy|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['no', 'No'], ['cost', 'At cost'], ['sales_price', 'Sales price']]|

|sortable|True|

|store|True|

|string|Re-Invoice Costs|

|type|selection|

#Field: visible_expense_policy

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['purchase_ok']|

|exportable|True|

|groupable|False|

|manual|False|

|name|visible_expense_policy|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Re-Invoice Policy visible|

|type|boolean|

#Field: sales_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids.sales_count']|

|digits|[16, 2]|

|exportable|True|

|groupable|False|

|manual|False|

|name|sales_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Sold|

|type|float|

#Field: invoice_policy

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['type']|

|exportable|True|

|groupable|True|

|help|Ordered Quantity: Invoice quantities ordered by the customer.
Delivered Quantity: Invoice quantities delivered to the customer.|

|manual|False|

|name|invoice_policy|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['order', 'Ordered quantities'], ['delivery', 'Delivered quantities']]|

|sortable|True|

|store|True|

|string|Invoicing Policy|

|type|selection|

#Field: optional_product_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|(company_id and ['|', ('company_id', '=', False), ('company_id', 'parent_of', [company_id])] or ['|', ('company_id', '=', False), ('company_id', 'parent_of', '')]) + ([])|

|exportable|True|

|groupable|True|

|help|Optional Products are suggested whenever the customer hits *Add to Cart* (cross-sell strategy, e.g. for computers: warranty, software, etc.).|

|manual|False|

|name|optional_product_ids|

|readonly|False|

|relation|product.template|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Optional Products|

|type|many2many|

#Field: product_add_mode

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Configurator: choose attribute values to add the matching product variant to the order.
Grid: add several variants at once from the grid of attribute values|

|manual|False|

|name|product_add_mode|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['configurator', 'Product Configurator'], ['matrix', 'Order Grid Entry']]|

|sortable|True|

|store|True|

|string|Add product mode|

|type|selection|

#Field: service_to_purchase

|change_default|False|

|company_dependent|True|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|If ticked, each time you sell this product through a SO, a RfQ is automatically created to buy the product. Tip: don't forget to set a vendor on the product.|

|manual|False|

|name|service_to_purchase|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Subcontract Service|

|type|boolean|

#Field: landed_cost_ok

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Indicates whether the product is a landed cost: when receiving a vendor bill, you can allocate this cost on preceding receipts.|

|manual|False|

|name|landed_cost_ok|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Is a Landed Cost|

|type|boolean|

#Field: split_method_landed_cost

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Default Split Method when used for Landed Cost|

|manual|False|

|name|split_method_landed_cost|

|readonly|False|

|required|False|

|searchable|True|

|selection|[['equal', 'Equal'], ['by_quantity', 'By Quantity'], ['by_current_cost_price', 'By Current Cost'], ['by_weight', 'By Weight'], ['by_volume', 'By Volume']]|

|sortable|True|

|store|True|

|string|Default Split Method|

|type|selection|

#Field: hs_code

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Standardized code for international shipping and goods declaration.|

|manual|False|

|name|hs_code|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|HS Code|

|translate|False|

|trim|True|

|type|char|

#Field: country_of_origin

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|Rules of origin determine where goods originate, i.e. not where they have been shipped from, but where they have been produced or manufactured.
As such, the ‘origin’ is the 'economic nationality' of goods traded in commerce.|

|manual|False|

|name|country_of_origin|

|readonly|False|

|relation|res.country|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Origin of Goods|

|type|many2one|

#Field: rating_last_value

|aggregator|avg|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids', 'rating_ids.rating', 'rating_ids.consumed']|

|exportable|True|

|groupable|True|

|groups|base.group_user|

|manual|False|

|name|rating_last_value|

|readonly|True|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Rating Last Value|

|type|float|

#Field: rating_last_feedback

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.feedback']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_last_feedback|

|readonly|True|

|related|rating_ids.feedback|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Rating Last Feedback|

|translate|False|

|type|text|

#Field: rating_last_image

|attachment|False|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.rating_image']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_last_image|

|readonly|True|

|related|rating_ids.rating_image|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Rating Last Image|

|type|binary|

#Field: rating_count

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.res_id', 'rating_ids.rating']|

|exportable|True|

|groupable|False|

|manual|False|

|name|rating_count|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Rating count|

|type|integer|

#Field: rating_avg

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.res_id', 'rating_ids.rating']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_avg|

|readonly|True|

|required|False|

|searchable|True|

|sortable|False|

|store|False|

|string|Average Rating|

|type|float|

#Field: rating_avg_text

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_avg']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_avg_text|

|readonly|True|

|required|False|

|searchable|False|

|selection|[['top', 'Satisfied'], ['ok', 'Okay'], ['ko', 'Dissatisfied'], ['none', 'No Rating yet']]|

|sortable|False|

|store|False|

|string|Rating Avg Text|

|type|selection|

#Field: rating_percentage_satisfaction

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.res_id', 'rating_ids.rating']|

|exportable|True|

|groupable|False|

|manual|False|

|name|rating_percentage_satisfaction|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Rating Satisfaction|

|type|float|

#Field: rating_last_text

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['rating_ids.rating_text']|

|exportable|True|

|groupable|False|

|groups|base.group_user|

|manual|False|

|name|rating_last_text|

|readonly|True|

|related|rating_ids.rating_text|

|required|False|

|searchable|True|

|selection|[['top', 'Satisfied'], ['ok', 'Okay'], ['ko', 'Dissatisfied'], ['none', 'No Rating yet']]|

|sortable|False|

|store|False|

|string|Rating Text|

|type|selection|

#Field: website_description

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_description|

|readonly|False|

|required|False|

|sanitize|True|

|sanitize_attributes|False|

|sanitize_style|False|

|sanitize_tags|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Description for the website|

|strip_classes|False|

|strip_style|False|

|translate|True|

|type|html|

#Field: description_ecommerce

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|description_ecommerce|

|readonly|False|

|required|False|

|sanitize|True|

|sanitize_attributes|False|

|sanitize_style|False|

|sanitize_tags|True|

|searchable|True|

|sortable|True|

|store|True|

|string|eCommerce Description|

|strip_classes|False|

|strip_style|False|

|translate|True|

|type|html|

#Field: alternative_product_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|(company_id and ['|', ('company_id', '=', False), ('company_id', 'parent_of', [company_id])] or ['|', ('company_id', '=', False), ('company_id', 'parent_of', '')]) + ([])|

|exportable|True|

|groupable|True|

|help|Suggest alternatives to your customer (upsell strategy). Those products show up on the product page.|

|manual|False|

|name|alternative_product_ids|

|readonly|False|

|relation|product.template|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Alternative Products|

|type|many2many|

#Field: accessory_product_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|(company_id and ['|', ('company_id', '=', False), ('company_id', 'parent_of', [company_id])] or ['|', ('company_id', '=', False), ('company_id', 'parent_of', '')]) + ([])|

|exportable|True|

|groupable|True|

|help|Accessories show up when the customer reviews the cart before payment (cross-sell strategy).|

|manual|False|

|name|accessory_product_ids|

|readonly|False|

|relation|product.product|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Accessory Products|

|type|many2many|

#Field: website_size_x

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_size_x|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Size X|

|type|integer|

#Field: website_size_y

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_size_y|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Size Y|

|type|integer|

#Field: website_ribbon_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|website_ribbon_id|

|readonly|False|

|relation|product.ribbon|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Ribbon|

|type|many2one|

#Field: website_sequence

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Determine the display order in the Website E-commerce|

|manual|False|

|name|website_sequence|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Website Sequence|

|type|integer|

#Field: public_categ_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|True|

|help|The product will be available in each mentioned eCommerce category. Go to Shop > Edit Click on the page and enable 'Categories' to view all eCommerce categories.|

|manual|False|

|name|public_categ_ids|

|readonly|False|

|relation|product.public.category|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Website Product Category|

|type|many2many|

#Field: product_template_image_ids

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|[]|

|domain|[]|

|exportable|True|

|groupable|False|

|manual|False|

|name|product_template_image_ids|

|readonly|False|

|relation|product.image|

|relation_field|product_tmpl_id|

|required|False|

|searchable|True|

|sortable|False|

|store|True|

|string|Extra Product Media|

|type|one2many|

#Field: base_unit_count

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['product_variant_ids', 'product_variant_ids.base_unit_count']|

|exportable|True|

|groupable|True|

|help|Display base unit price on your eCommerce pages. Set to 0 to hide it for this product.|

|manual|False|

|name|base_unit_count|

|readonly|False|

|required|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Base Unit Count|

|type|float|

#Field: base_unit_id

|change_default|False|

|company_dependent|False|

|context|{}|

|default_export_compatible|False|

|depends|['product_variant_ids', 'product_variant_ids.base_unit_count']|

|domain|[]|

|exportable|True|

|groupable|True|

|help|Define a custom unit to display in the price per unit of measure field.|

|manual|False|

|name|base_unit_id|

|readonly|False|

|relation|website.base.unit|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Custom Unit of Measure|

|type|many2one|

#Field: base_unit_price

|change_default|False|

|company_dependent|False|

|currency_field|currency_id|

|default_export_compatible|False|

|depends|['list_price', 'base_unit_count']|

|exportable|True|

|groupable|False|

|manual|False|

|name|base_unit_price|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Price Per Unit|

|type|monetary|

#Field: base_unit_name

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|['uom_name', 'base_unit_id.name']|

|exportable|True|

|groupable|False|

|help|Displays the custom unit for the products if defined or the selected unit of measure otherwise.|

|manual|False|

|name|base_unit_name|

|readonly|True|

|required|False|

|searchable|False|

|sortable|False|

|store|False|

|string|Base Unit Name|

|translate|False|

|trim|True|

|type|char|

#Field: compare_list_price

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|currency_field|currency_id|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|help|Add a strikethrough price to your /shop and product pages for comparison purposes.It will not be displayed if pricelists apply.|

|manual|False|

|name|compare_list_price|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Compare to Price|

|type|monetary|

#Field: allow_out_of_stock_order

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|allow_out_of_stock_order|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Continue selling when out-of-stock|

|type|boolean|

#Field: available_threshold

|aggregator|sum|

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|available_threshold|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Show Threshold|

|type|float|

#Field: show_availability

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|show_availability|

|readonly|False|

|required|False|

|searchable|True|

|sortable|True|

|store|True|

|string|Show availability Qty|

|type|boolean|

#Field: out_of_stock_message

|change_default|False|

|company_dependent|False|

|default_export_compatible|False|

|depends|[]|

|exportable|True|

|groupable|True|

|manual|False|

|name|out_of_stock_message|

|readonly|False|

|required|False|

|sanitize|True|

|sanitize_attributes|True|

|sanitize_style|False|

|sanitize_tags|True|

|searchable|True|

|sortable|True|

|store|True|

|string|Out-of-Stock Message|

|strip_classes|False|

|strip_style|False|

|translate|True|

|type|html|


