from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock


# class LinkValue(blocks.StructValue):
#     '''Add logic for our links'''

#     def url(self):
#         internal_page = self.get('internal_page')
#         external_link = self.get('external_link')

#         if internal_page:
#             return internal_page.url
#         if external_link:
#             return external_link
#         return '#'


class TitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Titolo", max_length=500)

    class Meta:
        template = 'blocks/block_title.html'
        icon = 'title'
        label = 'Titolo sezione'


class ContentBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(label="Contenuto", features=['h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'link'])

    class Meta:
        template = 'blocks/block_content.html'
        icon = 'pilcrow'
        label = 'Contenuto'


class BlockquoteBlock(blocks.StructBlock):
    quote = blocks.CharBlock(label="Citazione", max_length=500)
    cite = blocks.CharBlock(label="Fonte", max_length=255, required=False)

    class Meta:
        template = 'blocks/block_blockquote.html'
        icon = 'openquote'
        label = 'Citazione'


class TableBlock(blocks.StructBlock):
    table = TableBlock()

    class Meta:
        template = 'blocks/block_table.html'
        icon = 'table'
        label = 'Tabella'


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Immagine")
    caption = blocks.CharBlock(label="Didascalia", max_length=255, required=False)

    class Meta:
        template = 'blocks/block_image.html'
        icon = 'image'
        label = 'Immagine'


class VideoBlock(blocks.StructBlock):
    video = DocumentChooserBlock(label="Video mp4", help_text="Inserisci un tuo video mp4")

    class Meta:
        template = 'blocks/block_video.html'
        icon = 'media'
        label = 'Video mp4'


class VideoEmbedBlock(blocks.StructBlock):
    embed_video = EmbedBlock(label="Video embed", help_text="Inserisci un video da YouTube/Vimeo")

    class Meta:
        template = 'blocks/block_video.html'
        icon = 'media'
        label = 'Video embed'
