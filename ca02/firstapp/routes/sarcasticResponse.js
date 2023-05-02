/*
    codeCommentGen.js -- Router for the codeCommentGen
*/
const express = require('express');
const router = express.Router();

const {Configuration, OpenAIApi } = require('openai');

const ChatGPT = require('../models/ChatGPT');
const configuration = new Configuration({
    apiKey: process.env.OPENAI_APIKEY,
})
const openai = new OpenAIApi(configuration);

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
        next()
    } else {
        res.redirect('/login')
    }
}

router.get('/sarcasticResponse', isLoggedIn, async (req, res, ) => {
    ChatGPT.findOne().sort({date:-1})
        .then(function(doc) {
            console.log(doc);
            res.render('sarcasticResponse', {dialogue : doc});
        });
});


router.post('/sarcasticResponse',
    isLoggedIn,
    async (req, res, ) => {
        const prompt = "Ask us any question to get an answer";

        const completion = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: prompt,
        });
        const answer = completion.data.choices[0].text;
        const conversation = new ChatGPT (
            {
                date: new Date(),
                prompt: prompt,
                response: completion.data.choices[0].text.trim(),
                userId: req.user._id
            })
        await conversation.save();
        res.redirect('/sarcasticResponse')
    });


module.exports = router;
