from odoo import api,models,fields
import requests

class MailCallTrigger(models.Model):
    _name = 'mail.call.trigger'
    _description = 'Mail Call Trigger'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    mail_body = fields.Html('Body')
    mail_subject = fields.Char('Subject')
    status = fields.Char('Status')
    trigger_time = fields.Datetime('Time')
    email_to = fields.Char('Email To')

    @api.model
    def message_new(self, msg, custom_values=None):
        """ Create new support ticket upon receiving new email"""
        sub = 'EMERGENCY'
        email = 'OUTGOING987'
        mail_from = (msg.get('from').upper())
        mail_subject = (msg.get('subject')).upper()
        if (email in mail_from) and (sub in mail_subject):
            sms = 'http://api.accessyou.com/voice/send.php?' + 'accountno=' + str(32001030) + '&' + 'pwd=' + str(92072454) + '&' + 'phone=' + str(
                                                        85292072454) + '&' + 'wavfile=' + '1234.wav'

            val = requests.get(sms)
            default ={}
            # Extract the name from the from email if you can
            from_date = msg.get('date')

            default['trigger_time'] = from_date
            default['email_to'] = msg.get('to')
            default['mail_body'] = msg.get('body')
            default['mail_subject'] = msg.get('subject')
            default['status'] = 'Successful'
            return super(MailCallTrigger, self).message_new(msg, custom_values=default)

    def tf_js_fetch_now(self):
        server_id = self.env['fetchmail.server'].search([('state', '=', 'done')], limit=1)
        if server_id:
            server_id.fetch_mail()