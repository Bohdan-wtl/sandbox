class PaymentPage:
    def __init__(self, page):
        # Billing Information

        # Frame payment
        self.iframe_payment = page.locator("//div[@id='payment-element']/div/iframe")
        self.frame_payment = self.iframe_payment.content_frame
        self.card_number = self.frame_payment.locator("//input[@id='Field-numberInput']")
        self.expiry_date_input = self.frame_payment.locator("//input[@id='Field-expiryInput']")
        self.cvc_code_input = self.frame_payment.locator("//input[@id='Field-cvcInput']")
        self.exit_from_payment_frame = page.locator("body")
        self.submit_payment_button = page.locator("//button[@id='submit']")

        # Billing info
        self.iframe_billing = page.locator("//div[@id='address-element']/div/iframe")
        self.frame_billing = self.iframe_billing.content_frame
        self.billing_full_name_input = self.frame_billing.locator("//input[@id='Field-nameInput']")
        self.billing_country_input = self.frame_billing.locator("//input[@id='Field-countryInput']")
        self.billing_address_line1_input = self.frame_billing.locator("//input[@id='Field-addressLine1Input']")
        self.billing_city_input = self.frame_billing.locator("//input[@id='Field-localityInput']")
        self.billing_postal_code_input = self.frame_billing.locator("//input[@id='Field-postalCodeInput']")

        self.billing_info_continue_button = page.locator("//button[@id='infoSubmit']")

    def make_payment(self):
        self.card_number.fill("4242424242424242")
        self.expiry_date_input.fill("0127")
        self.cvc_code_input.fill("127")
        self.exit_from_payment_frame.click()

    def click_on_submit_payment_button(self):
        self.submit_payment_button.wait_for(state='visible', timeout=40000)
        self.submit_payment_button.click()

