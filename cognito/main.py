

# class CognitoIdentityProviderWrapper:
#     """Encapsulates Amazon Cognito actions"""
#     def __init__(self, cognito_idp_client, user_pool_id, client_id, client_secret=None):
#         """
#         :param cognito_idp_client: A Boto3 Amazon Cognito Identity Provider client.
#         :param user_pool_id: The ID of an existing Amazon Cognito user pool.
#         :param client_id: The ID of a client application registered with the user pool.
#         :param client_secret: The client secret, if the client has a secret.
#         """
#         self.cognito_idp_client = cognito_idp_client
#         self.user_pool_id = user_pool_id
#         self.client_id = client_id
#         self.client_secret = client_secret
#
#
#     # Esta funcion sirve para registrar y para logearse
#     def sign_up_user(self, user_name, password, user_email):
#         """
#         Signs up a new user with Amazon Cognito. This action prompts Amazon Cognito
#         to send an email to the specified email address. The email contains a code that
#         can be used to confirm the user.
#
#         When the user already exists, the user status is checked to determine whether
#         the user has been confirmed.
#
#         :param user_name: The user name that identifies the new user.
#         :param password: The password for the new user.
#         :param user_email: The email address for the new user.
#         :return: True when the user is already confirmed with Amazon Cognito.
#                  Otherwise, false.
#         """
#         try:
#             kwargs = {
#                 'ClientId': self.client_id, 'Username': user_name, 'Password': password,
#                 'UserAttributes': [{'Name': 'email', 'Value': user_email}]}
#             if self.client_secret is not None:
#                 kwargs['SecretHash'] = self._secret_hash(user_name)
#             response = self.cognito_idp_client.sign_up(**kwargs)
#             confirmed = response['UserConfirmed']
#         except ClientError as err:
#             if err.response['Error']['Code'] == 'UsernameExistsException':
#                 response = self.cognito_idp_client.admin_get_user(
#                     UserPoolId=self.user_pool_id, Username=user_name)
#                 logger.warning("User %s exists and is %s.", user_name, response['UserStatus'])
#                 confirmed = response['UserStatus'] == 'CONFIRMED'
#             else:
#                 logger.error(
#                     "Couldn't sign up %s. Here's why: %s: %s", user_name,
#                     err.response['Error']['Code'], err.response['Error']['Message'])
#                 raise
#         return confirmed
#
#
#     def confirm_user_sign_up(self, user_name, confirmation_code):
#         """
#         Confirms a previously created user. A user must be confirmed before they
#         can sign in to Amazon Cognito.
#
#         :param user_name: The name of the user to confirm.
#         :param confirmation_code: The confirmation code sent to the user's registered
#                                   email address.
#         :return: True when the confirmation succeeds.
#         """
#         try:
#             kwargs = {
#                 'ClientId': self.client_id, 'Username': user_name,
#                 'ConfirmationCode': confirmation_code}
#             if self.client_secret is not None:
#                 kwargs['SecretHash'] = self._secret_hash(user_name)
#             self.cognito_idp_client.confirm_sign_up(**kwargs)
#         except ClientError as err:
#             logger.error(
#                 "Couldn't confirm sign up for %s. Here's why: %s: %s", user_name,
#                 err.response['Error']['Code'], err.response['Error']['Message'])
#             raise
#         else:
#             return True
#
#
#         def resend_confirmation(self, user_name):
#         """
#         Prompts Amazon Cognito to resend an email with a new confirmation code.
#
#         :param user_name: The name of the user who will receive the email.
#         :return: Delivery information about where the email is sent.
#         """
#         try:
#             kwargs = {
#                 'ClientId': self.client_id, 'Username': user_name}
#             if self.client_secret is not None:
#                 kwargs['SecretHash'] = self._secret_hash(user_name)
#             response = self.cognito_idp_client.resend_confirmation_code(**kwargs)
#             delivery = response['CodeDeliveryDetails']
#         except ClientError as err:
#             logger.error(
#                 "Couldn't resend confirmation to %s. Here's why: %s: %s", user_name,
#                 err.response['Error']['Code'], err.response['Error']['Message'])
#             raise
#         else:
#             return delivery
