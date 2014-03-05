(function($) {
  "use strict";

  var experience = {
    init: function() {
      this.extract_dom();
      this.events();
    },

    /**
     * Retrieve and store all valid jQuery elements from the DOM
     */
    extract_dom: function() {
      this.$mainwrapper = $("#experience-wrapper");
      this.$logoWrapper = $("#experience-technologies");
      this.$logos = $(".technology-story", this.$logoWrapper);
      this.$btnCloseStory = $("#story-close");
      this.$currentStory = this.$prevStory = this.$nextStory = $();
    },

    story_get_prev_or_last: function() {
      var $prev = this.$currentStory.prev(".technology-story");
      return $prev.length ? $prev : this.$logos.filter(":last");
    },

    story_get_next_or_first: function($from) {
      var $next = this.$currentStory.next(".technology-story");
      return $next.length ? $next : this.$logos.filter(":first");
    },

    /**
     * Show a specific user story
     */
    story_show: function($elm) {
      if(!this.$currentStory.is($elm)) {

        // Remove classes set on previous active & navigation stories
        this.$currentStory.removeClass("active story-visible");
        this.$prevStory.add(this.$nextStory).removeClass("navigate prev next story-visible");

        // Set the new current story and use this to calculate the previous / next ones
        this.$currentStory = $elm.addClass("active story-visible");
        this.$prevStory = this.story_get_prev_or_last().addClass("navigate prev story-visible");
        this.$nextStory = this.story_get_next_or_first().addClass("navigate next story-visible");

        // Start a fresh time out to add the loaded class to the wrapper
        clearTimeout(this.loadedTimeout);
        this.$logoWrapper.removeClass("loaded");
        this.loadedTimeout = setTimeout($.proxy(this.story_set_loaded, this), 500);

        // If a story wasn't active before this, initialise keyboard events
        if(!this.storyActive) {
          this.$logoWrapper.addClass("story");
          this.storyActive = true;
          this.story_init_keyevents();
        }
      }
    },

    /**
     * Set the current story as loaded. This is when the CSS animations are complete
     */
    story_set_loaded: function() {
      this.$logoWrapper.addClass("loaded");
    },

    /**
     * Track key events when a story is active
     */
    story_init_keyevents: function() {
      var _this = this;
      $(window).on("keydown", function(e) {
        switch(e.keyCode) {
          // left
          case 37:
            _this.story_set_prev_active();
            break;
          case 39:
            _this.story_set_next_active();
            break;
          case 27:
            _this.story_close();
            break;
        }
      });
    },

    /**
     * Make previous story active
     */
    story_set_prev_active: function() {
      this.story_show(this.$prevStory);
    },

    /**
     * Make next story active
     */
    story_set_next_active: function() {
      this.story_show(this.$nextStory);
    },

    /**
     * Close the active story, returning to grid
     */
    story_close: function() {
      this.$logoWrapper.removeClass("story loaded");
      this.$logos.attr("class", "technology-story");
      this.$currentStory = $();
      this.storyActive = false;
      $(window).off("keydown");
    },

    /**
     * Initialise events
     */
    events: function() {
      var _this = this;

      $("body").on("click", $.proxy(this.story_close, this));
      this.$logoWrapper.on("click", function(e) {
        e.stopPropagation();
      });

      this.$btnCloseStory.on("click", $.proxy(this.story_close, this));
      this.$logos.on("click", function() {
        _this.story_show($(this));
      });
    }
  };

  /**
   * Once the DOM is ready, initialise the experience
   */
  $("document").ready(function() {
    if($("#experience-wrapper").length) {
      experience.init();
    }
  });

})(jQuery);
