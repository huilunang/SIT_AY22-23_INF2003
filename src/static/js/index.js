function bootstrap_alert(alertType, message) {
  var html = `
    <div class="alert alert-${alertType} alert-dismissible fade show" role="alert">
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `;

  document.getElementById("alert").innerHTML = html;
}
