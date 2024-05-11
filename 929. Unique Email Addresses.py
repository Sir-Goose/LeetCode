class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain = email.split('@')
            if '+' in local_name:
                local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            unique_emails.add(local_name + '@' + domain)
        return len(unique_emails)

