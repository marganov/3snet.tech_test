from ..links.page_urls import FORM_PAGE_URL

class FormPageLocators:
    FORM_TITLE = "h3.mb-5"
    EMAIL_INPUT = "#email"
    NAMES_INPUT = "#names"
    MESSAGE_TEXT_INPUT = "#message_text"
    SELECT_OPTION_OFFER = "#type"
    SELECT_OPTION_SALE = "#type > option:nth-child(2)"
    SELECT_OPTION_DISCOUNT = "#type > option:nth-child(3)"
    SUBMIT_BUTTON = "button.btn.btn-primary.btn-lg.btn-block"

