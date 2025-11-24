// Copyright 2023-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
// License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

odoo.define('website_academy_library.books', function (require) {
'use strict';

    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    console.log('website_academy_library.books loaded');
    var QWeb = core.qweb;
    var _t = core._t;

    publicWidget.registry.LibraryBookPublicWidget = publicWidget.Widget.extend({
        selector: '.book-detail-container',
        events: {
            'click button.js_show_more_book': '_onButtonShowMoreBook',
        },
        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.baseBookUrl = "/libraries/books/";
            this.responseRpcValue = undefined;
        },
        _onButtonShowMoreBook: function(ev) {
            var self = this;
            var bookId = $(ev.currentTarget).data('book_id');
            // RPC that call a controller route type JSON
            this._rpc({
                route: this.baseBookUrl + bookId,
                params: {},
            }).then(function (resultData) {
                console.log("resultData: ", resultData);
                self.$el.find(".show-more-info-book").html(resultData.rendered_template);
            });

            // RPC that call a model method
            // this._rpc({
            //     model: 'res.book',
            //     method: 'search_read',
            //     kwargs: {
            //         domain: [['id', '=', value]],
            //         fields: ['id', 'name'],
            //     },
            // }).then(function (resultDataModel) {
            //     console.log("resultDataModel: ", resultDataModel);
            // });
        },
    });

    return publicWidget.registry.LibraryBookPublicWidget;

});
