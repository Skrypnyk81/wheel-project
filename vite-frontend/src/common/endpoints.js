const baseEndpoint="/api/v1/wheels/"

const endpoints = {
    createWheel: `${baseEndpoint}create-wheel/`,
    detailWheel: `${baseEndpoint}detail-wheel/`,
    listWheel: `${baseEndpoint}list-wheel/`,
    filterWheel: `${baseEndpoint}filter-list-wheel/`,
    createOrder: `${baseEndpoint}create-order/`,
};

export{ endpoints }