(function($) {
  "use strict";

  var main = {
    init: function() {
      this.extract_dom();
      this.events();
    },

    /**
     * Retrieve and store all valid jQuery elements from the DOM
     */
    extract_dom: function() {
      this.$nav = $("#nav"),
      this.$navToggle = $("#nav-toggle");
    },

    /**
     * Prevent nav clicks from propagating to the body and removing it's active state
     */
    nav_click: function(e) {
      e.stopPropagation();
    },

    /**
     * Toggle the navigation, using an optional explicit boolean to set manually
     */
    nav_toggle: function(explicit) {
      var newState = typeof explicit == "boolean" ? explicit : !this.$nav.hasClass("active");
      this.$nav.toggleClass("active", newState);
    },

    /**
     * Initialise events
     */
    events: function() {
      $("body").on("click", $.proxy(this.nav_toggle, this, false));
      this.$nav.on("click", $.proxy(this.nav_click, this));
      this.$navToggle.on("click", $.proxy(this.nav_toggle, this));
    }
  };

  /**
   * Once the DOM is ready, initialise the blog
   */
  $("document").ready(function() {
    main.init();
  });

})(jQuery);
