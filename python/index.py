#!F:/Python27/python.exe
import socket
import header
#HTML code for Front end Page
htmlCode = """\
      <div class="span12">
            <!--Form containing item parameters and seller credentials needed for SetExpressCheckout Call-->
            <form class="form" action="paypal_ec_redirect.py" method="POST">
               <div class="row-fluid">
                  <div class="span4 inner-span">
                        <!--Demo Product details -->
                        <table>
                        <tr><h3> IMPORTED ICE CUBE FROM NORTH POLE </h3></tr>
                        <tr><img src="http://%s/img/ice-cube.jpg" width="300" height="250"/></tr>
                        <tr><td><p class="lead"> Buyer Credentials:</p></td></tr>
                        <tr><td>Email-id:&nbsp;&nbsp;&nbsp;<input type="text" id="buyer_email" name="buyer_email" readonly></input> </td></tr>
                        <tr><td>Password:<input type="text" id="buyer_password" name="buyer_password" readonly></input></td></tr>
                        </table>
                  </div>
                  <div class="span8 inner-span">
                        <p class="lead"> Item Specifications:</p>
                        <div class="span5">
                        <table>
                        <tr><td>Item Name:</td><td><input type="text" name="L_PAYMENTREQUEST_0_NAME0" value="Ice cube from North Pole" readonly></input></td></tr>
                        <tr><td>Item ID: </td><td><input type="text" name="L_PAYMENTREQUEST_0_NUMBER0" value="V3RYC01D" readonly></input></td></tr>
                        <tr><td>Description:</td><td><input type="text" name="L_PAYMENTREQUEST_0_DESC0" value="1 second for your cold drink" readonly></input></td></tr>
                        <tr><td>Quantity:</td><td><input type="number" id="Quantity" name="L_PAYMENTREQUEST_0_QTY0" value="1" min="1" onchange=update()></input></td></tr>
                        <tr><td>Price:</td><td><input type="text" id="Price" name="L_PAYMENTREQUEST_0_AMT0" value="10" readonly></input></td></tr>
                        <tr><td>Tax:</td><td><input type="text" id="Tax" name="PAYMENTREQUEST_0_TAXAMT" value="2" readonly></input></td></tr>
                        </table>
                        </div>
                        <div class="span6">
                        <table>
                        <tr><td>Shipping Amount:</td><td><input type="text" id="Fee1" name="PAYMENTREQUEST_0_SHIPPINGAMT" value="3" readonly></input></td></tr>
                        <tr><td>Handling Amount:</td><td><input type="text" id="Fee2" name="PAYMENTREQUEST_0_HANDLINGAMT" value="2" readonly></input></td></tr>
                        <tr><td>Shipping Discount:</td><td><input type="text" id="Discount" name="PAYMENTREQUEST_0_SHIPDISCAMT" value="-5" readonly></input></td></tr>
                        <tr><td>Insurance Amount:</td><td><input type="text" id="Fee3" name="PAYMENTREQUEST_0_INSURANCEAMT" value="2" readonly></input></td></tr>
                        <tr><td>Total Amount:</td><td><input type="text" id="Total" value="10" readonly></input></td></tr>
                        <tr><td><input type="hidden" name="LOGOIMG" value="http://%s/img/logo.jpg"></input></td></tr>
                        <tr><td>Currency Code:</td><td><select id="currencyCodeType" name="currencyCodeType">
            <option selected value="USD">USD</option>
            <option value="BRL">BRL</option>
            <option value="CAD">CAD</option>
            <option value="CZK">CZK</option>
            <option value="DKK">DKK</option>
            <option value="EUR">EUR</option>
            <option value="HKD">HKD</option>
            <option value="HUF">HUF</option>
            <option value="ILS">ILS</option>
            <option value="JPY">JPY</option>
            <option value="NOK">NOK</option>
            <option value="MXN">MXN</option>
            <option value="NZD">NZD</option>
            <option value="PHP">PHP</option>
            <option value="PLN">PLN</option>
            <option value="GBP">GBP</option>
            <option value="SGD">SGD</option>
            <option value="SEK">SEK</option>
            <option value="CHF">CHF</option>
            <option value="TWD">TWD</option>
            <option value="THB">THB</option>
            <option value="TRY">TRY</option>
                        </select><br></td></tr>
                        <tr><td>Payment Type: </td><td><select>
                                                           <option value="Sale">Sale</option>
                                                           <option value="Authorization">Authorization</option>
                                                           <option value="Order">Order</option>
                                                         </select><br></td></tr>
                        </table>
                        </div>
                        <div class="span1"></div>
                        <div class="span5">
                        <table>
                        <tr><td colspan="2"><input type="image" src="https://www.paypalobjects.com/webstatic/en_US/i/buttons/checkout-logo-large.png" alt="Check out with PayPal"/></td>
                  <td style=" white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"> -- OR -- </td>
                  <td ><input type="Submit" alt="Proceed to Checkout" class="btn btn-primary btn-large" value="Proceed to Check out" name="checkout"/></td></tr>
                        </table>
                        </div>
                  </div>
               </div>
            </form>
      </div>
      <!--Script to dynamically choose a seller and buyer account to render on index page-->
      <script type="text/javascript">
       function getRandomNumberInRange(min, max) {
          return Math.floor(Math.random() * (max - min) + min);
       }
      
      var buyerCredentials = [{"email":"ron@hogwarts.com", "password":"qwer1234"},
                        {"email":"sallyjones1234@gmail.com", "password":"p@ssword1234"},
                        {"email":"joe@boe.com", "password":"123456789"},
                        {"email":"hermione@hogwarts.com", "password":"123456789"},
                        {"email":"lunalovegood@hogwarts.com", "password":"123456789"},
                        {"email":"ginnyweasley@hogwarts.com", "password":"123456789"},
                        {"email":"bellaswan@awesome.com", "password":"qwer1234"},
                        {"email":"edwardcullen@gmail.com", "password":"qwer1234"}];
      var randomBuyer = getRandomNumberInRange(0,buyerCredentials.length);
      
      document.getElementById("buyer_email").value =buyerCredentials[randomBuyer].email;
      document.getElementById("buyer_password").value =buyerCredentials[randomBuyer].password;
      function update(){
            document.getElementById('Total').value = parseInt(document.getElementById('Quantity').value)*(parseFloat(document.getElementById('Price').value))+parseFloat(document.getElementById('Tax').value)
                                                +parseFloat(document.getElementById('Fee1').value)+parseFloat(document.getElementById('Fee2').value)+parseFloat(document.getElementById('Fee3').value)
                                                +parseFloat(document.getElementById('Discount').value);
      }
      
      </script>""" %(socket.gethostbyname(socket.gethostname()), socket.gethostbyname(socket.gethostname()))
print htmlCode
import footer
