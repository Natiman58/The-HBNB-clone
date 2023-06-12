$(document).ready(function() {
    var selectedAmenities = [];

    $('input[type="checkbox"]').change(function() {
      var selectedCheckbox = $(this);
      var amenityName = selectedCheckbox.data('name');
      var isChecked = selectedCheckbox.is(':checked');

      if (isChecked) {
        selectedAmenities.push(amenityName);
      } else {
        var index = selectedAmenities.indexOf(amenityName);
        if (index !== -1) {
          selectedAmenities.splice(index, 1);
        }
      }

      if (selectedAmenities.length > 0 && selectedAmenities.length < 4) {
        $('.amenities h4').text(selectedAmenities.join(', '));
      } else if (selectedAmenities.length >= 4) {
        var truncatedText = selectedAmenities.slice(0, 3).join(', ') + ' ...';
        $('.amenities h4').text(truncatedText);
      } else {
        $('.amenities h4').text('');
      }
    });
  });
