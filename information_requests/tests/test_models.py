from datetime import date

from freezegun import freeze_time
from model_bakery import baker


class TestInformationRequest:
    def test_count_days_until_a_reply_was_given(self):
        request = baker.prepare(
            "information_requests.InformationRequest",
            sent_at=date(2021, 1, 1),
            replied_at=date(2021, 1, 16),
        )

        assert request.days_without_reply == 15

    @freeze_time("2021-01-31")
    def test_count_days_without_reply(self):
        request = baker.prepare(
            "information_requests.InformationRequest",
            sent_at=date(2021, 1, 1),
        )

        assert request.days_without_reply == 30
