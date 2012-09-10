% if error:
  <strong>${error}</strong> : <p>${error_description}</p>
% else:
  Do you authorize this?

  <form method="POST">
    <input type="hidden" value="${request.url}" name="url"></input>
    <button type="submit">ALLOW</button> | DENY
  </form>
% endif 
